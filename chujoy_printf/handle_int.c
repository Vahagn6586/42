/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   handle_d.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vrafyan <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/11 17:57:24 by vrafyan           #+#    #+#             */
/*   Updated: 2026/03/11 17:57:25 by vrafyan          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	handle_int(va_list *arg)
{
	int	val;
	int	count;

	val = va_arg(*arg, int);
	count = ft_putnbr(val);
	return (count);
}
